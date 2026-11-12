from App import create_app
from App import home, projects

if __name__ == "__main__":
    app = create_app()

    app.register_blueprint(home.base)
    app.register_blueprint(projects.base)

    app.run(host='0.0.0.0', port=5001, debug=True)