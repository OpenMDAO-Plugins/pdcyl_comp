
Using the PDCyl Openmdao Wrapper
================================

The PdcylComp component is a file-wrap of PDCyl, an aircraft structural weight
estimation code. This distribution includes the files you need to run PdcylComp in
OpenMDAO. It does not include a source or binary distribution of Pdcyl, which
it is assumed you already have installed in your local environment.

PdcylComp can be imported from ``pdcyl_comp.py``, which should reside in the
site-packages directory of your activated Python environment once it is
installed.

::

    from pdcyl_comp.pdcyl_comp import PdcylComp

PdcylComp exposes all variables from the input file as inputs. Please see the
source documentation for further information on the input variables.

The following variables are extracted from the PDCyl output file and propagated
to the PDCyl component's outputs.

::

    wwingt       -  Total Wing Structural Weight
    wfuselaget   -  Fuselage Total Structural Weight
        
Generally, the easiest way for you to import your existing PDCyl models
into the OpenMDAO component is to use the ``load_model`` method.

::

    pdcyl_comp.load_model('my_model.in')
    
When the PDCylComp is instantiated, the defaults for the variables are all zero, so
a model must be loaded or the values must be set manually before running.

If your local PDCyl install is not in your system path, you will need
to tell OpenMDAO where to find it as per the following example:

::

    pdcyl_comp.command = '/home/ktmoore1/work/PDCyl/PDCyl'
