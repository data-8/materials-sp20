test = {
  'name': 'q4_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(bootstrap_utility_left) != type(...), type(bootstrap_utility_left) != None])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([type(bootstrap_utility_right) != type(...), type(bootstrap_utility_right) != None])
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
