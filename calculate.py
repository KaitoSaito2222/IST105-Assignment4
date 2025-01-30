import sys
import math

# Check if a, b, and c are numeric. If not, return an error message.
def validate_input(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        return True, (a, b, c)
    except ValueError:
        return False, "Error: All inputs must be numeric values."

def calculate_result(a, b, c):
    # If a is less than 1, display a message indicating that the input is too small.
    if a < 1:
        return "<p class='error'>Error: Input 'a' is too small</p>"
    # If b is equal to 0, indicate that it will not affect the result.
    if b == 0:
        return "<p>Note: 'b' is zero and will not affect the result</p>"
    # If c is negative, provide a specific error message.
    if c < 0:
        return "<p class='error'>Error: 'c' cannot be negative</p>"
    
    # Calculate c^3
    c_cubed = c ** 3

    # Apply final calculations based on c^3 value
    if c_cubed > 1000:
        final_result = math.sqrt(c_cubed) * 10
    else:
        final_result = math.sqrt(c_cubed) / a
    
    # Add b to the final result
    final_result += b
    
    result = f"""
    <div class='results'>
        <h3>Calculation Results:</h3>
        <p>Value of c³: {c_cubed}</p>
        <p>If the result of c^3 is greater than 1000, Multiply the square root of c^3 by 10.</p>
        <p>Otherwise, divide the square root by a.</p>
        <p>Final result: {final_result}</p>
    </div>
    """
    return result

def main():
    # Generate HTML output
    html_output = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Calculation Results</title>
        <style>
            .error { color: red; }
            .results { margin: 20px 0; }
        </style>
    </head>
    <body>
    """

    html_output_end = """
        <p><a href="form.php">Calculate Again</a></p>
    </body>
    </html>
    """

    if len(sys.argv) != 4:
        html_output += "<p class='error'>Error: Please provide exactly 3 inputs</p>"
        print(html_output + html_output_end)
        sys.exit(1)
    
    # Validate input
    is_valid, result = validate_input(sys.argv[1], sys.argv[2], sys.argv[3])
    
    if not is_valid:
        html_output += f"<p class='error'>{result}</p>"
        print(html_output + html_output_end)
        sys.exit(1)
    
    a, b, c = result
    html_output += calculate_result(a, b, c)
    print(html_output + html_output_end)

if __name__ == "__main__":
    main()