# General Language Model
Introduction to LLMs using Google's Gemini API

In this project, a fine-tuned model was created to make a Formula One commentary based on the user's input. Ideally, it will continue where the user ended their input.

## Libraries
| Library | Use case |
| --- | --- |
| `google.generativeai` | To utilize Google's Gemini API
| `random` | To generate a random number to make the model id unique |
| `pandas` | To create a dataframe based on the model's snapshots
| `seaborn` | To create a lineplot to visualize the loss curve of the tuned model

## Files 
| File | Description |
| --- | --- |
| `dataset.py` | It contains a sparse dataset to fine-tune the model. It also stores the prompts that will be used for few-shot prompting with the fine-tuned model.
| `model.ipynb` | A jupyter notebook that contains the descriptive process of creating the fine-tuned model.

## Instructions
Before using the jupyter notebook, the user must have access to my Google AI Studio.

With the right permissions, simply run the jupyter notebook to use the fine-tuned model.

Have fun! 👾
## Example
<code>

    *** Sample input ***
    " I like Gemini  "
    
    *** Sample output ***
    """
        I like Gemini, but the real star of the show today is the Taurus of the track, the Red Bull racing machine.Max Verstappen, the fiery Dutchman, is behind the wheel, and he's on a mission to conquer. The air crackles with anticipation as the lights go out, and the pack of Formula One cars explode off the starting grid. Verstappen, starting from pole position, rockets off the line, his Red Bull a blur of blue and red as he devours the asphalt. 
    """
    
</code>