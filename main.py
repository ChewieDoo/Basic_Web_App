from website import create_app

app = create_app()
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

if __name__ == '__main__':
    app.run(debug=True)
