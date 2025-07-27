from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("mcpexample")

@mcp.tool()
def test():
    print("example")

def main():
    print("Hello from mcpexample!")


if __name__ == "__main__":
    main()
