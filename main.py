import click

from controllers.parse_image import ParseImage
from usecases.map_exporter import MapExporter


@click.command()
@click.option(
    "--output",
    default="./output",
    help="The output path for the collisions generated from the image",
)
@click.option(
    "--size",
    default="800x600",
    help="The output size for the generated map",
)
@click.argument("image_src", default="")
def map_identifier(output: str, size: str, image_src: str) -> None:
    """Extract a map from a image and convert it to a file containing information about elements and collision"""
    map_dimensions = size.split("x")
    if len(map_dimensions) != 2:
        raise ValueError("Invalid map size")

    ParseImage(
        MapExporter(collision_groups=[]), dimensions=tuple(map_dimensions)
    ).parse(image_src=image_src, output=output)


if __name__ == "__main__":
    map_identifier()
