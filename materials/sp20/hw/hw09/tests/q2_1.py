test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your resample should have the same number of rows as the original sample;
          >>> simulate_resample(observations).num_rows
          17
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your resample should only have the ;
          >>> simulate_resample(observations).labels[0] == observations.labels[0] 
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
