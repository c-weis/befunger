# befunger
**befunger** is a [Befunge](https://en.wikipedia.org/wiki/Befunge) interpreter written in Python.
I wrote it in an afternoon with my friend [Jan Steinebrunner](https://www.jan-steinebrunner.com/).
We set the boundary conditions of the code plane to be periodic.
The code and variable stack may be visualised at runtime.

## Code samples
We obtained sample code from the [Esolangs page for befunge](https://esolangs.org/wiki/Befunge). With the exception of *more_or_less.bf*, we did not modified the code.

## Usage
You may run a befunge file *filename*
by running:
```shell
python befunger.py filename
```
We recommend running the number guessing game *more_or_less.bf*.

You can watch the code as it is being executed by further specifying a float *step-size*. If you do, **befunger** will pause for *step-size* seconds between consecutive steps. For example, to run *more_or_less.bf* with a delay *0.05* seconds per step, run:
```shell
python befunger.py more_or_less.bf 0.05
```

Alternatively, you can use **befunger** in your python file 
by calling
```python
import befunger
```
and execute *.bf* files by calling 
```python
befunger.execute(filename, step_size)
```
where *step_size* is optional, as above.
