def generatorArg(*args):
    return f''.join(f'{item}' for item in args)


def generatorKwarg(**kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    return f' '.join(f' {c}="{v}"' for c, v in kwargs.items())


def tag(tag, *args, **kwargs):
    return f'<{tag}{generatorKwarg(**kwargs)}>{generatorArg(*args)}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
        )