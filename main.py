from fasthtml.common import *

lorem_md = """
# Lorem ipsum

Lorem ipsum dolor sit amet, **consectetur** adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur.

### Another section

- Curabitur pretium tincidunt lacus.
- Nulla gravida orci a odio.
- Nullam varius, turpis et commodo pharetra.
- Lorem ipsum dolor sit amet.
"""

# Built-in headers for Markdown rendering & code highlighting:
my_hdrs = (
    MarkdownJS(),
    Style("""
      /* Limit container width on larger screens */
      .container {
          max-width: 600px;
          margin: 0 auto;
      }
      /* Optionally, for smaller screens, let it expand */
      @media (max-width: 768px) {
          .container {
              max-width: 95%;
          }
      }
    """)
)

# fast_app sets up a minimal FastHTML application with defaults (PicoCSS, etc.)
app, rt = fast_app(hdrs=my_hdrs)

@rt("/")
def get():
    # Titled() sets <title> and an <h1>.
    # We wrap the markdown in a Div with cls="marked"; MarkdownJS() converts it to HTML on load.
    return Titled("Lorem Demo",
        Main(cls="container")(
            Div(lorem_md, cls="marked")
        )
    )

serve()