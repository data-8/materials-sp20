test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(one_resampled_percentage(votes)) in set([float, np.float64]) 
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 35 <= one_resampled_percentage(votes) <= 65
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
