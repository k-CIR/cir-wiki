---
title: Plot head-channel alignment in FieldTrip
taags: [FieldTrip, scripting]
---

Recommendation: always plot the head models together with the head points and sensors as a sanity check that the process went well.

Easy code snippet you can copy paste to your script:

/// tab | FieldTrip
```matlab
%% Plot all aligned: MEG
figure; hold on
ft_plot_sens(grad)
ft_plot_headshape(headshape)
ft_plot_headmodel(headmodel)
ft_plot_axes([], 'unit', 'cm');
```

![]({{ picture_path }}/meg_check.jpg)
///