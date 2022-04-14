def generic_model_mutation_process(model, data, id=None, home_world=None, commit=True):
    u"""
    Adds or update a register on the model received.

    Parameters
    ----------
    model: Model
        the model to execute the action.
    data: Dict
        the data to add or update in the DB.
    id: Int
        identifier of the register to make an
        update.Default value in None.
    commit: Boolean
        Flag to know if the action
        should be executed.
        Default value in True.

    Returns
    -------
    item: Model
        the item that was created or update
        in the DB.
    """
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)

    else:
        item = model(**data)

    if commit:
        item.save()

    return item
