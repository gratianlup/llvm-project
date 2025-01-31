#  Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
#  See https://llvm.org/LICENSE.txt for license information.
#  SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

try:
    from ..ir import *
    from ..dialects import transform
except ImportError as e:
    raise RuntimeError("Error loading imports from extension module") from e

from typing import Optional, overload, Union


class EmptyTensorToAllocTensorOp:
    """Specialization for EmptyTensorToAllocTensorOp class."""

    @overload
    def __init__(
        self,
        transformed_type: Type,
        target: Union[Operation, OpView, Value],
        *,
        loc=None,
        ip=None
    ):
        ...

    @overload
    def __init__(self, target: Union[Operation, OpView, Value], *, loc=None, ip=None):
        ...

    def __init__(
        self,
        transformed_type_or_target: Type,
        target_or_none: Optional[Union[Operation, OpView, Value]] = None,
        *,
        loc=None,
        ip=None
    ):
        if isinstance(transformed_type_or_target, Type):
            transformed_type = transformed_type_or_target
            target = target_or_none
        else:
            transformed_type = transform.OperationType.get("bufferization.alloc_tensor")
            target = transformed_type_or_target

        super().__init__(
            transformed_type,
            target,
            loc=loc,
            ip=ip,
        )


class OneShotBufferizeOp:
    """Specialization for OneShotBufferizeOp class."""

    @overload
    def __init__(
        self,
        transformed_type: Type,
        target: Union[Operation, OpView, Value],
        *,
        allow_return_allocs: Optional[bool] = None,
        allow_unknown_ops: Optional[bool] = None,
        bufferize_function_boundaries: Optional[bool] = None,
        create_deallocs: Optional[bool] = None,
        test_analysis_only: Optional[bool] = None,
        print_conflicts: Optional[bool] = None,
        memcpy_op: Optional[str] = None,
        loc=None,
        ip=None
    ):
        ...

    @overload
    def __init__(self, target: Union[Operation, OpView, Value], *, loc=None, ip=None):
        ...

    def __init__(
        self,
        transformed_type_or_target: Type,
        target_or_none: Optional[Union[Operation, OpView, Value]] = None,
        *,
        allow_return_allocs: Optional[bool] = None,
        allow_unknown_ops: Optional[bool] = None,
        bufferize_function_boundaries: Optional[bool] = None,
        create_deallocs: Optional[bool] = None,
        test_analysis_only: Optional[bool] = None,
        print_conflicts: Optional[bool] = None,
        memcpy_op: Optional[str] = None,
        loc=None,
        ip=None
    ):
        if isinstance(transformed_type_or_target, Type):
            transformed_type = transformed_type_or_target
            target = target_or_none
        else:
            transformed_type = transform.AnyOpType.get()
            target = transformed_type_or_target

        super().__init__(
            transformed_type,
            target,
            allow_return_allocs=allow_return_allocs,
            allow_unknown_ops=allow_unknown_ops,
            bufferize_function_boundaries=bufferize_function_boundaries,
            create_deallocs=create_deallocs,
            test_analysis_only=test_analysis_only,
            print_conflicts=print_conflicts,
            memcpy_op=memcpy_op,
            loc=loc,
            ip=ip,
        )
