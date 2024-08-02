# parser-playground

Just me trying to figure out how (certain) parsers work.
I try as much as I can to **extreamly** simplefy the parsing algorithms.

## Language

The test language tries to be implemented in a _simple_ calculator with following symbols:

| symbol | action         |
| ------ | -------------- |
| +      | addition       |
| -      | subtraction    |
| \*     | multiplication |
| /      | division       |

### Syntax _a_:

```
expr   = unary ("+" | "-" | "*" | "/") ( unary | expr ) ;
unary  = "-" unary | number ;
number = digit+ ( "." digit+ )? ;
digit  = "0" ... "9" ;

```

### Syntax _b_:

```
expr   = (unary| expr) ("+" | "-" | "*" | "/") unary ;
unary  = "-" unary | number ;
number = digit+ ( "." digit+ )? ;
digit  = "0" ... "9" ;

```

Allowed examples:

```
1 + 2 * 3
4 * 5 + 1 - 1
4 - 2 - 2
-15 + 15 * 2
2 / 2 + 2
```

## Parsers:

### Implemented:

- Top-down:
  - Recursive decent parsing
- Bottom-up:
  - (empty)

### To Implement:

- Top-down:
  - Pratt parsing
  - Packrat parsing
  - PEG parsing
  - ...
- Bottom-up:
  - Pika Parser
  - ...

## Sources:

- https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html
- https://abarker.github.io/typped/pratt_parsing_intro.html
- https://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/
- https://github.com/lukehutch/pikaparser
- https://arxiv.org/pdf/2005.06444
