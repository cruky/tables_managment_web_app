import os
import csv

from flask import Flask, render_template, request, flash, redirect, url_for, get_flashed_messages
from werkzeug.utils import secure_filename

from authorization import auth_bp, login_required
from db_operations import get_session, add_asset, get_count_of_db, get_all_rows_from_assets

# https://pythonise.com/series/learning-flask/flask-uploading-files
# https://gis.stackexchange.com/questions/58229/interacting-between-openlayers-and-python
# https://stackoverflow.com/questions/15691525/python-mapnik-example-on-how-to-render-a-map-with-a-gps-track-on-it
ALLOWED_EXTENSIONS = {'csv'}
CSV_DELIMITER = ';'
MODEL_COLUMNS = ['IDENTIFIER', 'TYPE', 'LAT', 'LONG']

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "SekretnyKodzik")
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 # Max 2 megabytes file
app.config["UPLOAD_FOLDER"] = './file_storage'

app.register_blueprint(auth_bp)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def read_csv(csvfile):
    '''Read csv file and return list of dicts'''
    data = []
    with open(csvfile, 'r', encoding='utf-8') as file:
        csv_file = csv.DictReader(file, delimiter=';')
        for csv_row in csv_file:
            csv_input_columns = ([column.upper() for column in (csv_row.keys())])
            if all(elem in csv_input_columns for elem in MODEL_COLUMNS):
                data.append(dict(csv_row))
            else:
                return False
    # Return only lowercase column names
    data = [{k.lower(): v for k, v in csv_row.items()} for csv_row in data]
    return data


@app.route('/')
def redirect_user():
    '''Redirect the user to our main page'''
    return redirect(url_for('upload_file'))


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    '''Get the file from the user'''
    flash_messages = get_flashed_messages()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error')
            app.logger.error('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # if not os.path.isfile(file_path)
            file_content = read_csv(file_path)
            os.remove(file_path)
            if file_content is False:
                flash('Wrong File, please check file schema', 'error')
                return redirect(request.url)
            elif not file_content:
                flash("Empty File, we couldn't identify any data", 'error')
                return redirect(request.url)
            else:
                try:
                    session = get_session()
                    init_asset_count = get_count_of_db(session)
                    for record in file_content:
                        add_asset(session, record.get('identifier'), record.get('type'), record.get('lat'),
                                  record.get('long'), request.remote_addr)
                    assets_ingested = get_count_of_db(session) - init_asset_count
                    flash(f'You ingested {assets_ingested} assets', 'info')
                    return redirect(url_for('view_table'))
                except Exception as error_obj:
                    error_msg = f"{type(error_obj).__name__}Something went wrong with inserting data \n {error_obj.args[0]}"
                    flash(error_msg, 'error')
                    app.logger.error(error_msg)
                    return redirect(request.url)

    return render_template('upload.html', flash_messages=flash_messages)

@app.route('/table')
@login_required
def view_table():
    '''Show the data in tables'''
    flash_messages = get_flashed_messages()
    session = get_session()
    assets_data = get_all_rows_from_assets(session)
    return render_template('assets_view.html', assets_data=assets_data, flash_messages=flash_messages)


if __name__ == "__main__":
    app.run(debug=False)
