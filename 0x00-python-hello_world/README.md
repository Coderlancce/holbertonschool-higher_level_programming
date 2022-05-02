# 0x00. Python - Hello, World

In python for print a text you can use print(), that function have some parameters how {}, in that space you can add datatype to put here, its a function similarity to printf with %:

### Example

#### In python with print:

num = 21
print(" I have {} years old.".format(num))

or

num = 21
print(f"I have {num} years old.")

#### In c with printf:

num = 21;
printf("I have %d years old.", num);

You can game with all that modes and interactions, you can get a part of a text if you know the cordenades

### Example

#### In python with print

text = "Hello World"
text = text[:5]
print("{}")

Hello

#### In c with printf

i = 0;
char *text = "Hello World";
for(i = 0; text[i] != 5; i++)
	printf("", text[i]);

Hello