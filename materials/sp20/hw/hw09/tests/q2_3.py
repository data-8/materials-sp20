test = {
  'name': 'q2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(example_estimates) == 10000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 850 < np.mean(example_estimates) < 1100
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.count_nonzero(np.diff(example_estimates)) >= 1
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
