from flask import Blueprint, render_template, abort

base = Blueprint('projects', __name__)

projects = {
    # "ray-tracer": {
    #     "title": "Ray Tracer",
    #     "subtitle": "A software ray tracer written in C++",
    #     "date": "2026",
    #     "status": "Completed",
    #     "technologies": ["C++", "OpenMP", "Computer Graphics"],

    #     "description": """
    #     A ray tracing application developed as part of my
    #     Advanced Rendering coursework. The project explores
    #     ray-triangle intersections, lighting and material shading.
    #     """,

    #     "overview": """
    #     This project implements a ray tracing pipeline and compares it to a rasterisation approach.
    #     It includes primary, secondary and shadow ray generation as well as Blinn-Phong illumination
    #     """,

    #     "features": [
    #         "Ray-triangle intersection testing",
    #         "Barycentric coordinate interpolation",
    #         "Blinn-Phong shading",
    #         "Multi-threaded rendering using OpenMP"
    #         ""
    #     ],

    #     "images": [
    #         {
    #             "src": "images/raytracer/render1.png",
    #             "caption": "Example rendered scene"
    #         },
    #         {
    #             "src": "images/raytracer/render2.png",
    #             "caption": "Lighting and shading demonstration"
    #         }
    #     ],

    #     "pdf": None,

    #     "video": None,

    #     "github": "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY",
    #     "readme": "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/blob/main/README.md",

    #     "links": [
    #         {
    #             "title": "GitHub Repository",
    #             "url": "https://github.com/YOUR_USERNAME/YOUR_REPOSITORY"
    #         }
    #     ]
    # },

    "multi-style-rendering": {
        "title": "Multi Style NPR Rendering Pipeline",
        "subtitle": "A framework to render multiple NPR styles in a performant manner for Unity3D",
        "date": "2026",
        "status": "Completed",
        "technologies": ["C#", "HLSL", "Unity3D", "RenderGraph", "Scriptable Render Pipeline"],

        "description": """
            For my bachelor's dissertation I investigated the impact of region-based localisation on combining multiple npr
            effects in a single realtime scene. I carried this out using Unity's scriptable render pipeline.
        """,

        "overview": """

        """,

        "features": [
            "CPU Bounding-Box Localisation",
            "GPU Bounding-Box Localisation",
            "GPU Tiling Localisation"
            "Scriptable Render Passes"
        ],

        "images": [
            {
                "src": "images/multi-style-renderer/renderpipeline.png",
                "caption": "Proposed Pipeline"
            },
        ],

        "videos": [
            {
                "src": "videos/multi-style-renderer/DemoVideo.mp4",
                "caption": "Demonstration of the multi-style rendering pipelinevyeo"
            }
        ],

        "pdf": "documents/multi-style-renderer/EDMONDS26-FINAL.pdf",

        "github": "https://github.com/BigRorzUni/MultipleStyleRendering",

        "links": [
            {
                "title": "GitHub Repository",
                "url": "https://github.com/BigRorzUni/MultipleStyleRendering"
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