import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("Sreshthak15/final", "main"),
                            commands=["echo '#!/bin/bash' | cat - /codebuild/output/tmp/script.sh > temp && mv temp /codebuild/output/tmp/script.sh",
                                "source .venv/bin/activate",
                                "python -m pip install -r requirements.txt",
                                "cdk --version",
                                "cdk synth"]
                        )
                    )