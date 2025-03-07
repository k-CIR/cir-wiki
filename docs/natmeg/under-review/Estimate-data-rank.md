It is important to know the rank of the data for several common MEG processing steps, such as source reconstruction and data whitening. This is particularly important when you have processed your data with MaxFilter which reduce the rank of the data drastically.

After MaxFilter the rank is usually around 72. The rank is reduced further if you remove, e.g. ICA components during pre-processing.

## In MNE-Python
MNE-Python has a build-in function to estimate rank of the data called `mne.compute_rank`. See the full documentation here: https://mne.tools/stable/generated/mne.compute_rank.html?highlight=rank#mne.compute_rank

Some (!) MNE-Python functions will estimate the rank on the fly. but sometimes it will assume the rank is equal to the number of channels rather than calculate it. It is safer to use `mne.compute_rank` and make sure the rank is in the ballpark of what you expect.

## In FieldTrip
In `ft_sourceanalysis` you can specify the rank as "kappa" in the `cfg`. Calculate Kappa like this:

````Matlab
%% Calculate Kappa
cfg = [];
cfg.covariance          = 'yes';
cfg.covariancewindow    = 'all';
cfg.channel             = 'MEG';
data_cov = ft_timelockanalysis(cfg, epo);

[u,s,v] = svd(data_cov.cov);
d       = -diff(log10(diag(s)));
d       = d./std(d);
kappa   = find(d>5,1,'first');
fprintf('Kappa = %i\n', kappa)
`````

Taken from this tutorial: https://www.fieldtriptoolbox.org/workshop/paris2019/handson_sourceanalysis/
