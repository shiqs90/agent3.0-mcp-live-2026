from fastmcp import FastMCP

mcp= FastMCP("Warm-Up Server")

@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}! Welcome to MCP."

@mcp.tool
def add_numbers(a: int, b: int, c: int) -> int:
    """Add three numbers together."""
    return a + b + c

if __name__ == "__main__":
    mcp.run()