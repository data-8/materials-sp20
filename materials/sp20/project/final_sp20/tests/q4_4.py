test = {
  'name': 'q4_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.round(compute_municipal_cooperative_difference(electricity), 2) == -4284.59
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you're not hardcoding; use the `tbl` argument in your function;
          >>> np.round(compute_municipal_cooperative_difference(electricity.take(np.arange(10))), 2) == -1288.10
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
