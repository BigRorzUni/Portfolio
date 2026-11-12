from flask import Blueprint, render_template, abort

base = Blueprint('projects', __name__)

projects = {
    "ray-tracer": {
        "title": "Ray Tracer",
        "subtitle": "A software ray tracer written in C++",
        "date": "2026",
        "status": "Completed",
        "technologies": ["C++", "OpenMP", "Computer Graphics"],

        "description": """
        A ray tracing application developed as part of my
        Advanced Rendering coursework. The project explores
        ray-triangle intersections, lighting and material shading.
        """,

        "overview": """
        This project implements a ray tracing pipeline from scratch.
        It includes primary ray generation, triangle intersection,
        barycentric interpolation and Blinn-Phong illumination.
        """,

        "features": [
            "Ray-triangle intersection testing",
            "Barycentric coordinate interpolation",
            "Blinn-Phong shading",
            "Multi-threaded rendering using OpenMP"
        ],

        "images": [
            {
                "src": "images/raytracer/render1.png",
                "caption": "Example rendered scene"
            },
            {
                "src": "images/raytracer/render2.png",
                "caption": "Lighting and shading demonstration"
            }
        ],

        "video": None,

        "github": "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY",
        "readme": "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/blob/main/README.md",

        "links": [
            {
                "title": "GitHub Repository",
                "url": "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY"
            }
        ]
    }
}


@base.route("/projects/<project_id>")
def project_page(project_id):
    project = projects.get(project_id)

    if project is None:
        abort(404)

    return render_template("project.html", project=project)