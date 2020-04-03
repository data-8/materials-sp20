test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(max_estimate) in set([int, np.int32, np.int64])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max_estimate in observations.column(0)
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
