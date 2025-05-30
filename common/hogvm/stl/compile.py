# Run from project root (cd ../..)
# python3 -m common.hogvm.stl.compile

import glob
import json

from posthog.hogql import ast
from posthog.hogql.compiler.bytecode import create_bytecode, parse_program

source = "common/hogvm/stl/src/*.hog"
target_ts = "common/hogvm/typescript/src/stl/bytecode.ts"
target_py = "common/hogvm/python/stl/bytecode.py"

bytecodes: dict[str, [list[str], list[any]]] = {}

for filename in glob.glob(source):
    with open(filename) as file:
        code = file.read()
    basename = filename.split("/")[-1].split(".")[0]
    program = parse_program(code)
    found = False
    for declaration in program.declarations:
        if isinstance(declaration, ast.Function) and declaration.name == basename:
            found = True
            bytecode = create_bytecode(declaration.body, args=declaration.params).bytecode
            bytecodes[basename] = [declaration.params, bytecode]
    if not found:
        print(f"Error: no function called {basename} was found in {filename}!")  # noqa: T201
        exit(1)

with open(target_ts, "w") as output:
    output.write("// This file is generated by common/hogvm/stl/compile.py\n")
    output.write("export const BYTECODE_STL: Record<string, [string[], any[]]> = {\n")
    for name, (params, bytecode) in sorted(bytecodes.items()):
        output.write(f'  "{name}": [{json.dumps(params)}, {json.dumps(bytecode)}],\n')
    output.write("}\n")

with open(target_py, "w") as output:
    output.write("# This file is generated by common/hogvm/stl/compile.py\n")
    output.write("# fmt: off\n")
    output.write("BYTECODE_STL: dict[str, tuple[list[str], list]] = {\n")
    for name, (params, bytecode) in sorted(bytecodes.items()):
        output.write(f'  "{name}": ({json.dumps(params)}, {json.dumps(bytecode)}),\n')
    output.write("}\n")
    output.write("# fmt: on\n")
