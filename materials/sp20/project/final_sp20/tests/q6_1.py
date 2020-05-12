test = {
  'name': 'q6_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If this errored, you need to make sure you're using the arguments (i.e. weights) passed into the function,;
          >>> # and not hardcoding actors.column('Number of Movies');
          >>> np.round(weighted_rmse(make_array(1, 3, 5), make_array(2, 3, 4), make_array(1, 2, 3)), 2) == 0.67
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
