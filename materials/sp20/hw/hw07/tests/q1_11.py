test = {
  'name': 'q1_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your simulation isn't random.;
          >>> np.std([simulate_visited_area_codes() for _ in range(1000)]) > 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The sum of the items in model proportions should be 1;
          >>> model_proportions.item(0) + model_proportions.item(1)
          1.0
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
