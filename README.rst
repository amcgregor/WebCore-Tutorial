# WebCore Wiki Tutorial / Example

This is a sample Wiki application for WebCore, using marrow.mongo and RESTful Resource Dispatch.

In order to run the example, you will want to:

1. Create a virtual environment to house the project by running:

   `python3.5 -m venv wiki`

2. Activate the virtual environment:

   `cd wiki; source bin/activate`

3. Check out a copy of this code into the environment:

   `git clone -b wiki https://github.com/amcgregor/WebCore-Tutorial.git src`

4. Install the project, which will pull in any required dependencies:

   `cd src; python setup.py develop`

5. Make sure you have MongoDB running locally.

6. Run the example in the development web server:

   `python -m web.app.wiki`

That's about it.  To follow the tutorial, [browse the commit history on GitHub](https://github.com/amcgregor/WebCore-Tutorial/commits/wiki), starting at the oldest commit and working your way up.  Each commit is generally accompanied by an extensive commit message describing what changed and providing any further instructions related to that change.

Happy hacking!

