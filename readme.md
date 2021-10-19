# **`GETorade ⚡`** *by Passbird Research*


A Python micro 🤏 framework built on top of [`flask`](https://flask.palletsprojects.com/)🍾 to get you to *__ship__ near-production quality __APIs ASAP__* for your prototypes. Built by a backend engineer for backend and non-backend engineers alike.

It does so by WYSIWYG (What You See Is What You Get) routing, and making **opinionated** design, and code organization decisions for you.

![You'll thank me later](https://c.tenor.com/274hyAKNHckAAAAC/youll-thank-me-later-thankful.gif)


Works best with [*Replit*](https://replit.com/@tallmint/GETorade) (or *Docker* if you really want to productionize this). It [works well in production](https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/#run-with-a-production-server) thanks to [`waitress`](https://docs.pylonsproject.org/projects/waitress/en/latest/). .

## License

Do with it what you will, but be nice. Okay?

## Changelog

Conceived on the **Sixteenth** day of  **October** of the year **2021**.

Specification last updated on **18 October, 2021**

Debug help, Support, and Maintenance offered by [Naga Samineni](https://samineni.me), Passbird Research


## Quick Tutorial: Foo Bar Times
A repl for the project is hosted at [https://getorade.repl.passbird.co](https://getorade.repl.passbird.co)

Let's create a new API [https://getorade.repl.passbird.co/example/foo/bar?times=3](https://getorade.repl.passbird.co/example/foo/bar?times=3) that returns `"foo. bar. foo. bar. foo. bar. "` when called. I.e., it repeately prints `"foo. bar. "` till the specified number of times dictated by `times` 

PS: This API is not actually implemented in this repo and is left as an excersise for the reader.

### Step 1: Setup WYSIWYG route
The API path `example/foo/bar` translates literally to file `/routes/root/example/foo/bar.py` on disk, like so-

```
/routes
     |__ /root
            |__ /example
                     |__ /foo(+)
                           |__ bar.py(+)
```

where `(+)` above indicates newly created directories or files.

### Step 2: API Handler
`bar.py` would look something like this:

```Python

from flask import request

def main():
  timesStr = request.args.get('times')
  timesInt = int(timesStr)
  return "foo. bar. " * timesInt

```

### Step 3: Tying it all together
Finally, you need to create an empty `__init__.py` file at each of the newly created directories.

So the final directory structure would look something like this:

```
/routes
     |__ /root
            |__ /example
                     |__ /foo
                           |__ __init__.py(+)
                           |__ bar.py
```
That's all folks! Restart the application and you would now have built the new [https://getorade.repl.passbird.co/example/foo/bar?times=3](https://getorade.repl.passbird.co/example/foo/bar?times=3) API.

## Philosophy
After working in Corporate (Facebook, Twitter, Microsoft) for better part of a decade, I grew accustomed to certain luxuries of developer experience. Now that I'm out, I realized it's kinda annoying to not have that multi million dollar frameworks you can build off of.

In the perfect world, you'd just write the core business logic like a lambda function and hit publish and a multi million dollar team *someone* (\*cough\* multi million dollar team**S** \*cough\*) automagically takes care of CI/CD, Deployment, Hosting, Scaling, and all that jaaz. 

### So what is GETorade?
While I don't claim to fix all your devops and developer productivity voes, GETorade is a cute little framework I built for myself, optimized to be run on *Replit*.

It's been useful to me as I rapidly build and tear down experimental backends for [Passbird](https://passbird.co). 

GETorade helps you **ship** production quality APIs **ASAP**. In order to do this, it's **very opinionated** in design decisions, routing, and code organization (see next section on *What GETorade is not*)
- While **for now**, GETorade **only** handles **GET** requests, it will **NEVER** support anything other than **GET** and **POST** requests. GETorade is very opinionated this way, to get you to **SHIP ASAP**.

- WYSIWYG (What You See Is What You Get) routing - Defining `/routes/root/a/b/c.py`'s `main()` method automagically handles requests to `https://<domain>/a/b/c`. (more info in Tutorial below)

- If your route handlers (ex: `c.py` above) needs to handle non-trivial logic, GETorade opines that bulk of your non-trivial code should live in `/src/*` path, in line with the route handler path `/routes/root/*`.

If you're a purist, and hate *Replit*, you can download this as a zip, containerize it with docker and publish it on your own instead of using Replit. Whatever floats your boat.

### What GETorade is not
 

 GETorade **WONT** handle API level authentication. Instead, I insist you look at slapping an API management layer on top of the GETorade APIs you create (Here're some options: [Azure](https://azure.microsoft.com/en-us/services/api-management/), [GCP](https://cloud.google.com/apigee))

It's not Yet Another REST framework for Python. There're plenty out there already The goal we're shooting for is KISS (Keeping It Stupidly Simple).

It's not trying to hide the fact that it's built on top of Flask. Attempts to introduce abstractions to hide it break the KISS principle. More specifically, `request` object in GETorade is a [standard Flask Request object](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request), and `Response` (return value) is the [standard Flask Response object](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Response) and it shall **STAY THAT WAY**. 


## Quick examples
### Return JSON response
Checkout [`/routes/example/returnJson.py`](https://github.com/snagarohit/GETorade/blob/master/routes/root/example/returnJson.py) which handles  [https://getorade.repl.passbird.co/routes/example/returnJson](https://getorade.repl.passbird.co/example/returnJson) API. It returns

```JSON
{"1":true,"as":{"we":1},"hello":"world"}
```
### Read GET parameters from URL and Render in a Template
Checkout [`/routes/example/getParams.py`](https://github.com/snagarohit/GETorade/blob/master/routes/root/example/getParams.py) which is callable from [https://getorade.repl.passbird.co/example/getParams?name=Ray+Mysterio&age=619](https://getorade.repl.passbird.co/example/getParams?name=Ray+Mysterio&age=619). It returns

```HTML

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Passbird</title>
    <style>
      .centeredContent {
          position: absolute;
          top: 50%;
          left: 50%;
          -moz-transform: translateX(-50%) translateY(-50%);
          -webkit-transform: translateX(-50%) translateY(-50%);
          transform: translateX(-50%) translateY(-50%);
      }
    </style>
  </head>
  <body>
    <div class="centeredContent">
          <h4>Hi <b>Ray Mysterio</b>! You're 619 years old 😱</h4>  
    </div>
  </body>
</html>
```

### Using `src` directory for outsourcing **complicated** logic
Checkout [`/routes/example/complicated.py`](https://github.com/snagarohit/GETorade/blob/master/routes/root/example/complicated.py) which is callable from [https://getorade.repl.passbird.co/example/complicated?name=Dave&age=23](https://getorade.repl.passbird.co/example/complicated?name=Dave&age=23). It's supposed to display a birthday greetings to "Dave", with "23" candles. It outsources bulk of logic into [`/src/example/complicated/greetingProcessor.py`](https://github.com/snagarohit/GETorade/blob/master/src/example/complicated/greetingProcessor.py). This API returns

```HTML

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Passbird</title>
    <style>
      .centeredContent {
          position: absolute;
          top: 50%;
          left: 50%;
          -moz-transform: translateX(-50%) translateY(-50%);
          -webkit-transform: translateX(-50%) translateY(-50%);
          transform: translateX(-50%) translateY(-50%);
      }
    </style>
  </head>
  <body>
    <div class="centeredContent">
        <b>Happy birthday, Dave!</b><br/><b>Here's 23 candles for you:</b><br/>🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️🕯️   
    </div>
  </body>
</html>

```

**Note 1**: Notice that [`/src/example/complicated/greetingProcessor.py`](https://github.com/snagarohit/GETorade/blob/master/src/example/complicated/greetingProcessor.py) imports the supporting [`/src/example/complicated/_emojiArt.py`](https://github.com/snagarohit/GETorade/blob/master/src/example/complicated/__emojiArt.py) by fully qualified module name (fancy term for saying "full path to module"), like [`src.example.complicated._emojiArt`](https://github.com/snagarohit/GETorade/blob/master/src/example/complicated/greetingProcessor.py#L6). Checkout [`greetingProcessor.py`](https://github.com/snagarohit/GETorade/blob/master/src/example/complicated/greetingProcessor.py#L3-L5) for the "Why?"

**Note 2**: See how supporting code like [`__emojiArt.py`](https://github.com/snagarohit/GETorade/tree/master/src/example/complicated) are named starting with a double underscore `__`? It's an opinionated design decision to visually distinguish "externally imported" code like `greetingProcessor.py` from local supporting code like `__emojiArt.py`



## Bonus
This framework supports:
- Automatic static file hosting
  - Drop your file/directory under `/static` directory. See [`/static/favicon.ico`](https://github.com/snagarohit/GETorade/blob/master/static/favicon.ico) which can be reached by [https://getorade.repl.passbird.co/favicon.ico](https://getorade.repl.passbird.co/favicon.ico)
- `404` and index file (`/`) handling.
- Tempating support
  - See [`/routes/index.py`](https://github.com/snagarohit/GETorade/blob/master/routes/root/index.py#L4)


  ## Deployment Guide
  ### Local
```sh

% poetry update

Updating dependencies
Resolving dependencies... (0.3s)

Package operations: 7 installs, 0 updates, 0 removals

  • Installing markupsafe (2.0.1)
  • Installing click (8.0.3)
  • Installing itsdangerous (2.0.1)
  • Installing jinja2 (3.0.2)
  • Installing werkzeug (2.0.2)
  • Installing flask (2.0.2)
  • Installing waitress (2.0.0)

% poetry run python3 main.py
```
