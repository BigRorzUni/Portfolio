
from pathlib import Path
import shutil

from App import create_app
from App import home, projects


# Create Flask application
app = create_app()

# Register blueprints
app.register_blueprint(home.base)
app.register_blueprint(projects.base)

# Output directory
output_dir = Path("docs")

# Remove previous build
if output_dir.exists():
    shutil.rmtree(output_dir)

output_dir.mkdir()


def save_page(url, output_path):
    response = app.test_client().get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Failed to render {url}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(response.data)

    print(f"Generated: {output_path}")


# Generate homepage
save_page("/", output_dir / "index.html")


# Generate project pages
for project_id in projects.projects:
    save_page(
        f"/projects/{project_id}",
        output_dir / "projects" / project_id / "index.html"
    )


# Copy static assets
shutil.copytree(
    "App/static",
    output_dir / "static"
)

print("Static website generated successfully!")
