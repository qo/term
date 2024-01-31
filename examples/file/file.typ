#import "../../term.typ": term

#let ps1 = "$"
#let input = read("./in")
#let output = read("./out")

#let content = raw(ps1 + " " + input + output)

#figure(
  term(
    content: content
  ),
  caption: "Listing files in a directory",
)
