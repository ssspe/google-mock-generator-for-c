from __future__ import print_function
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from pycparser import c_parser, c_ast, parse_file

# A simple visitor for FuncDef nodes that prints the names and
# locations of function definitions.
class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
    #node.decl.type.args.params

        print ("Function name is", node.decl.name, "at", node.decl.coord)
        print ("    It's parameters name  and type is (are)")
        for params in (node.decl.type.args.params): ###FuncDef/Decl/FuncDecl/ParamList
            # Assign parameter name
            pname = params.name ###ParamList/Decl

            # Parameter is a pointer type of some kind
            if type(params.type) is c_ast.PtrDecl:
                # Parameter is a pointer to a pointer type - double indirection
                if type(params.type.type) is c_ast.PtrDecl:
                    ptype = params.type.type.type.type.names[0]  + "**" ###Decl/PtrDecl/PtrDecl/TypeDecl/IdentifierType
                # There is no double indirection
                else:
                    # Parameter is a pointer to a function type
                    if type(params.type.type) is c_ast.FuncDecl:
                        pname = str(params.type.type.type.type.names) + ' (*' ###Decl/PtrDecl/TypeDecl/IdentifierType
                        pname = pname + params.type.type.type.declname + ')' ###Decl/PtrDecl/FuncDecl/TypeDecl
                        ptype = ''
                        for subparams in params.type.type.args.params: ###Decl/PtrDecl/FuncDecl/ParamList
                            ptype = ptype + str(subparams.type.type.type.names) ###Typename/PtrDecl/TypeDecl/IdentifierType
                    # Parameter is a pointer type - single indirection
                    else:
                        ptype = params.type.type.type.names[0] + "*" ###Decl/PtrDecl/TypeDecl/IdentifierType

            # Parameter is a variable
            elif type(params.type.type) is c_ast.IdentifierType:
                ptype = params.type.type.names[0]

            print ("        ", pname, ptype)

        env = Environment(
            loader=FileSystemLoader('templates'))
        template = env.get_template('mytemplate.html')
        print( template.render(user="Hello"))

def show_func_calls(filename):
    ast = parse_file(filename, use_cpp=True,
                     cpp_path='gcc',
                     cpp_args=['-E', r'-Iutils/fake_libc_include'])
    v = FuncDefVisitor()
    v.visit(ast)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'hash.c'

    show_func_calls(filename)
