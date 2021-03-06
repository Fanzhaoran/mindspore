# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""InplaceAssign op"""
from mindspore.ops.op_info_register import op_info_register


@op_info_register("""{
    "op_name": "InplaceAssign",
    "imply_type": "AutoDiff",
    "fusion_type": "ELEMWISE",
    "attr": [
        {
            "name": "fake_output",
            "param_type": "optional",
            "type": "bool"
        }
    ],
    "inputs": [
        {
            "index": 0,
            "dtype": [
                "int32", "float16", "float32", "int32", "float16", "float32", "int32", "float16", "float32"
            ],
            "format": [
                "DefaultFormat", "DefaultFormat", "DefaultFormat", "NC1HWC0", "NC1HWC0", "NC1HWC0", "FracZ", "FracZ", "FracZ"
            ],
            "name": "x"
        },
        {
            "index": 1,
            "dtype": [
                "int32", "float16", "float32", "int32", "float16", "float32", "int32", "float16", "float32"
            ],
            "format": [
                "DefaultFormat", "DefaultFormat", "DefaultFormat", "NC1HWC0", "NC1HWC0", "NC1HWC0", "FracZ", "FracZ", "FracZ"
            ],
            "name": "y"
        },
        {
            "index": 2,
            "dtype": [
                "int32", "float16", "float32", "int32", "float16", "float32", "int32", "float16", "float32"
            ],
            "format": [
                "DefaultFormat", "DefaultFormat", "DefaultFormat", "NC1HWC0", "NC1HWC0", "NC1HWC0", "FracZ", "FracZ", "FracZ"
            ],
            "name": "z"
        }
    ],
    "outputs": [
        {
            "index": 0,
            "dtype": [
                "int32", "float16", "float32", "int32", "float16", "float32", "int32", "float16", "float32"
            ],
            "format": [
                "DefaultFormat", "DefaultFormat", "DefaultFormat", "NC1HWC0", "NC1HWC0", "NC1HWC0", "FracZ", "FracZ", "FracZ"
            ],
            "name": "output"
        }
    ]
}""")
def _inplace_assign_akg():
    """InplaceAssign AutoDiff register"""
    return
