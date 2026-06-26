from nova.modules.resolver import ModuleResolver
from nova.pipeline import create_interpreter


def run_source(
    source: str,
    input_provider=None,
    project_root=None,
):
    resolver = ModuleResolver(
        project_root=project_root,
    )

    interpreter = create_interpreter(
        source,
        input_provider=input_provider,
        resolver=resolver,
    )

    return interpreter.output


def run_file(
    path: str,
    input_provider=None,
    project_root=None,
):
    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    output = run_source(
        source,
        input_provider=input_provider,
        project_root=project_root,
    )

    return source, output