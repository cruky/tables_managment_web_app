from flask import Flask, request, redirect, url_for
from tabulate import tabulate
from pandas import DataFrame as pandasDataFrame
from pandas import read_csv as pandasReadCsv


app = Flask(__name__)


def read_csv(csvfile, conn):
    csv_df = pandasReadCsv(csvfile)
    csv_df.to_sql("table_name", conn, if_exists='append', index=False)


def dict_to_pandas_table_in_html(request_args):
    persons_df = pandasDataFrame(request_args, index=[request.remote_addr])
    print(tabulate(persons_df, headers="keys", tablefmt="grid"))
    pesons_html = persons_df.to_html(header="true", table_id="table")
    return pesons_html


@app.route('/')
def redirect_user():
    '''Redirect the user to our main page'''
    # return f'<a href="{request.base_url}table">Please go here to achieve anything</a>'
    return redirect(url_for('read_user_input'))


@app.route('/table')
def read_user_input():
    '''Get the request args, convert them to pandas data frame and then to html'''
    user_args = request.args

    if user_args and set(user_args.values()) != {None}:
        try:
            return dict_to_pandas_table_in_html(user_args)
        except Exception as error_obj:
            print(f"{type(error_obj).__name__}Ask Your Admin WTF \n {error_obj.args[0]}")

    example_link = f'<a href="{request.base_url}?name=Vladimir&surname=Flask&age=23">{request.base_url}?name=Vladimir&surname=Flask&age=23</a>'
    return f'<h1>Hey! Give me request arguments! \n\n\n Something like {example_link}</h1>'


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
