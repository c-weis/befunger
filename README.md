# befunger
**befunger** is a [Befunge](https://en.wikipedia.org/wiki/Befunge) interpreter written in Python.
I wrote it in an afternoon with my friend [Jan Steinebrunner](https://www.jan-steinebrunner.com/).
We set the boundary conditions of the code plane to be periodic.
The code and variable stack may be visualised at runtime.

![Animation of more_or_less.bf with visuals.](https://raw.githubusercontent.com/c-weis/befunger/main/animation.gif)

## Code samples
We obtained sample code from the [Esolangs page for Befunge](https://esolangs.org/wiki/Befunge). With the exception of *more_or_less.bf*, we did not modify the code.

## Usage
You may run a befunge file *filename* as follows:
```shell
python befunger.py filename
```
We recommend trying the number guessing game *more_or_less.bf*.

You can watch the code as it is being executed by further specifying a float *step-size*. If you do, **befunger** will pause for *step-size* seconds between consecutive steps. For example, to run *more_or_less.bf* with a delay of *0.05* seconds per step, run:
```shell
python befunger.py more_or_less.bf 0.05
```

Alternatively, you can use **befunger** to run befunge files from your own python program by calling
```python
import befunger

befunger.execute(filename, step_size)
```
where *step_size* is optional, as above.
