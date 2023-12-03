#import "term.typ": term

#figure(
  term(
    ps1: [`$`],
    input: [`ls -la`],
    output: [
    `total 140
drwxr-xr-x. 1 null null    48 Nov 30 01:11 .
drwx------. 1 null null  1032 Dec  3 18:30 ..
-rw-r--r--. 1 null null 23093 Nov 30 00:40 s1.png
-rw-r--r--. 1 null null 26076 Nov 30 01:02 s2.png
-rw-r--r--. 1 null null 42784 Nov 30 01:18 s3.png
-rw-r--r--. 1 null null 42735 Nov 30 01:12 s4.png`
    ],
  ),
  caption: [Listing all the files in the directory],
)
