import argparse
import json
from pathlib import Path

from geophires_x_schema_generator import GeophiresXSchemaGenerator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-in-src', required=False, choices=[True, False], default=True)
    parser.add_argument('--build-path', required=False)
    args = parser.parse_args()
    build_in_src = args.build_in_src

    build_dir = Path(Path(__file__).parent)
    if not args.build_in_src:
        build_dir = Path(Path(__file__).parent.parent.parent, 'build')

    if args.build_path:
        build_dir = Path(args.build_path)

    build_dir.mkdir(exist_ok=True)

    build_path = Path(build_dir, 'geophires-request.json')

    generator = GeophiresXSchemaGenerator()

    schema_json = generator.generate_json_schema()

    with open(build_path, 'w') as f:
        f.write(json.dumps(schema_json, indent=2))
        print(f'Wrote schema file to {build_path}.')

    rst = generator.generate_parameters_reference_rst()

    build_path_rst = Path(build_dir, 'parameters.rst')
    with open(build_path_rst, 'w') as f:
        f.write(rst)
