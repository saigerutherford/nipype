# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.dti import BEDPOSTX4GPU

def test_BEDPOSTX4GPU_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bpx_directory=dict(argstr='%s',
    usedefault=True,
    ),
    burn_period=dict(argstr='-b %d',
    ),
    bvals=dict(mandatory=True,
    ),
    bvecs=dict(mandatory=True,
    ),
    dwi=dict(mandatory=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fibres=dict(argstr='-n %d',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    jumps=dict(argstr='-j %d',
    ),
    mask=dict(mandatory=True,
    ),
    model=dict(argstr='-model %d',
    ),
    nlgradient=dict(argstr='-g',
    ),
    no_cuda=dict(argstr='-c',
    ),
    output_type=dict(),
    sampling=dict(argstr='-s %d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    weight=dict(argstr='-w %.2f',
    ),
    )
    inputs = BEDPOSTX4GPU.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BEDPOSTX4GPU_outputs():
    output_map = dict(bpx_out_directory=dict(),
    dyads=dict(),
    mean_fsamples=dict(),
    mean_phsamples=dict(),
    mean_thsamples=dict(),
    merged_fsamples=dict(),
    merged_phsamples=dict(),
    merged_thsamples=dict(),
    xfms_directory=dict(),
    )
    outputs = BEDPOSTX4GPU.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
