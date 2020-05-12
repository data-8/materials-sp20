test = {
  'name': 'q6_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(best_weighted_slope) != type(...), type(best_weighted_slope) != None])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([type(best_weighted_intercept) != type(...), type(best_weighted_intercept) != None])
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
