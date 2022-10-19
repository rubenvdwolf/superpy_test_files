<!-- Headings -->

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

<!-- Italics -->
*This text* is italic
_This text_ is also italic

<!-- Strong -->
**This text** is strong
__This text__ is also strong

<!-- Strikethrough -->
~~this text~~ is strikethrough

<!-- Horizontal Line -->
---
___


<!-- Blockquote -->
> this is a quote

<!-- Links -->
[Google](http://www.google.com)

[Google](http://www.google.com "Google")

<!-- UL -->
* Item 1
* Item 2
* Item 3
  * Nested item 1
  * Nested item 2


<!-- OL -->
1. Item 1
1. Item 2
1. Item 3

<!-- Inline code block -->
`<p>This is a paragraph in a code block</p>`

<!-- Images -->
![markdown logo](https://markdown-here.com/img/icon256.png)



<!-- Github Markdown -->

<!-- Github code blocks -->
```
npm install

npm start
```

```python
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

```

<!-- Table -->
| Name| Email|
|-----|------|
|Ruben|ruben.vanderwolf@gmail.com|
|Lisan|lisanvdk@gmail.com|


<!-- Task lists -->
* [x] Task 1
* [ ] Task 2 (incomplete)