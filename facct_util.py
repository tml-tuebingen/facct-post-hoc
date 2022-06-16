import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def viz_feature_attributions(attributions, feature_names, title, ylim=None, rotation=45):
    """ Produce the plots in the paper.
    """
    N = len(feature_names)
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.barplot(np.arange(N), attributions, color=sns.color_palette()[0])
    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel('Feature Attribution')
    ax.set_title(title)
    labels = [item.get_text() for item in ax.get_xticklabels()]
    ax.set_xticks(np.arange(N))
    ax.set_xticklabels(feature_names)
    if ylim is not None:
        plt.ylim(ylim)
    plt.xticks(rotation=rotation)
    
def extract_lime_attributions(exp, feature_names):
    """ Returns the attrbutions of a lime explanation as an array,
        ordered to match the ordering of the features in feature_names.
        
        exp: A LIME Explanation object 
        feature_names: List of feature names
        
        Returns: Feature attributions (list)
    """
    label = list(exp.as_map().keys())[0]
    exp = exp.as_list(label) 
    raw_attributions = [x for _, x in exp]
    lime_label_order = [x for x, _ in exp]
    
    attributions = [] # sort lime attributions according to feature_names
    for i in range(len(raw_attributions)):
        feature_name = feature_names[i]
        for idx,name in enumerate(lime_label_order):
            if feature_name in name:
                attributions.append(raw_attributions[idx])
            
    return attributions

def viz_lime_attr(exp, feature_names, ylim=None):
    attributions = extract_lime_attributions(exp, feature_names)
    viz_feature_attributions(attributions, feature_names, 'LIME Attributions', ylim=ylim)
    