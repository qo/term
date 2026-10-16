# term

A [Typst](https://github.com/typst/typst) template for drawing terminal windows with selectable text and vector graphics.

## Quick start

Download `term.typ` into your document's directory:

```sh
curl --fail --location https://raw.githubusercontent.com/qo/term/main/term.typ --output term.typ
```

Import the function and pass the terminal transcript as `content`:

```typst
#import "term.typ": term

#term(
  content: [`$ ls
term.typ`],
)
```

<img src="./examples/raw/raw.svg#svgView(viewBox(50, 50, 400, 200))" width="500" height="300" alt="A terminal window displaying an ls command and its output">

`content` accepts Typst content, including raw text. The transcript is supplied by you: the template does not run shell commands.

## Load a transcript from a file

Keep the command and its output together in a text file, such as `transcript.txt`:

```text
$ ls
term.typ
```

Use [`read`](https://typst.app/docs/reference/data-loading/read/) to load the file and [`raw`](https://typst.app/docs/reference/text/raw/) to preserve its formatting:

```typst
#import "term.typ": term

#term(content: raw(read("transcript.txt")))
```

The path passed to `read` is relative to the Typst file that calls it and must stay within the project's root. See the runnable [transcript example](examples/transcript/transcript.typ).

To capture fresh output, run the command yourself before compiling. For example, in a POSIX shell:

```sh
printf '$ ls\n' > transcript.txt
ls >> transcript.txt
typst compile document.typ
```

Only run commands you trust. Typst reads the saved output; compilation does not execute the transcript.

## Add a figure caption

```typst
#import "term.typ": term

#figure(
  term(content: [`$ ls
term.typ`]),
  caption: [Listing files in a directory],
)
```

## Examples

| Example | Description |
| --- | --- |
| [Raw content](examples/raw/raw.typ) | A transcript written directly in the document |
| [Text file](examples/transcript/transcript.typ) | A complete transcript loaded from one file |
| [Separate input and output](examples/file/file.typ) | A prompt, command, and saved output combined into one transcript |
| [Figure](examples/figure/figure.typ) | A terminal window with a caption |

When compiling an example from the repository root, allow it to import `term.typ` from that root:

```sh
typst compile --root . examples/transcript/transcript.typ transcript.svg
```

The template requests the `Roboto Mono` font. Install it for the intended appearance; Typst uses an available fallback if it is missing.

## Development checks

Run `python scripts/check-examples.py` to compile every example, or pass `--typst /path/to/typst` when the binary is not on your PATH. Outputs go to a temporary directory.

GitHub Actions runs the same check on pull requests, pushes to `main`, and every Monday, using both Typst 0.15.1 and the latest stable release. A failure on the latest release identifies a compatibility change to investigate before upgrading. The workflow is also available from Actions via **Run workflow**. Dependabot groups GitHub Actions updates into at most two open PRs for review; updates are not merged automatically.
