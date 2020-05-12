test = {
  'name': 'q7_1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(state_populations) != type(...), type(state_populations) != None])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([type(biggest_state_for_each_division) != type(...), type(biggest_state_for_each_division) != None])
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
