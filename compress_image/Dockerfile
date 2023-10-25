FROM public.ecr.aws/lambda/python:3.11

COPY Pipfile ${LAMBDA_TASK_ROOT}
COPY Pipfile.lock ${LAMBDA_TASK_ROOT}

COPY lambda_function.py ${LAMBDA_TASK_ROOT}

RUN pip install pipenv && \
    pipenv sync --system && \
    pip uninstall --yes pipenv

CMD [ "lambda_function.handler" ]
