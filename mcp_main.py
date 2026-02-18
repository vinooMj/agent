from mcp.server.fastmcp import FastMCP
import logging

mcp = FastMCP("basic_math_ops")

class MCPErrors(Exception):
    def __init__(self,code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='/tmp/mcp_server.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

@mcp.tool()
def add(a: int, b: int) -> int:
    '''
    Add two intergers and return the sum.

    Args:
        a: First Interger
        b: Second Integer
    
    Returns:
        The sum of a and b.
    '''
    logger.info(f"Adding {a} and {b}")
    res = a + b
    logger.info(f"Result {res}")
    return res

@mcp.tool()
def divide(a: int, b: int) -> float:
    '''
    divides two intergers and return the sum.

    Args:
        a: numerator
        b: deminator
    
    Returns:
        The result of division.
    '''
    if b == 0:
        raise MCPError(code = 400, message = "Division by zero is not allowed.")
    return a / b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    '''
    multiples two intergers and return the sum.

    Args:
        a: First interger number
        b: second interger number
    
    Returns:
        The result of multiplication.
    '''
    return a * b
 
if __name__ == "__main__":
    mcp.run()
