from App import create_app

if __name__ == "__main__":
    app = create_app()

    from App import home
    app.register_blueprint(home.base)

    app.run(host='0.0.0.0', debug=True)