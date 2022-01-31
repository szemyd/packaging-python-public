import argparse
from ast import Expression, literal_eval
from typing import Union

import libcst as cst
from libcst.codemod import CodemodContext, VisitorBasedCodemodCommand
from libcst.codemod.visitors import AddImportsVisitor


class ReplaceFunctionCommand(VisitorBasedCodemodCommand):

    # Add a description so that future codemodders can see what this does.
    DESCRIPTION: str = "Replaces the body of a function with pass."

    # @staticmethod
    # def add_args(arg_parser: argparse.ArgumentParser) -> None:
    #     # Add command-line args that a user can specify for running this
    #     # codemod.
    #     arg_parser.add_argument(
    #         "--string",
    #         dest="string",
    #         metavar="STRING",
    #         help="String contents that we should look for.",
    #         type=str,
    #         required=True,
    #     )
    #     arg_parser.add_argument(
    #         "--constant",
    #         dest="constant",
    #         metavar="CONSTANT",
    #         help="Constant identifier we should replace strings with.",
    #         type=str,
    #         required=True,
    #     )

    def __init__(self, context: CodemodContext) -> None:
        # Initialize the base class with context, and save our args. Remember, the
        # "dest" for each argument we added above must match a parameter name in
        # this init.
        super().__init__(context)


    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
        replace_function = cst.FunctionDef(
            name=updated_node.name, 
            params=cst.Parameters(), 
            body= cst.SimpleStatementSuite((cst.Pass(),)), 
            returns=None)
        
        return replace_function
