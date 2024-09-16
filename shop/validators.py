from rest_framework.serializers import ValidationError


class ShopValidator:
    def __init__(self, node_type, supplier, pk):
        self.node_type = node_type
        self.supplier = supplier
        self.pk = pk

    def __call__(self, instance):
        node_type = getattr(instance, self.node_type)
        supplier = getattr(instance, self.supplier)
        if node_type == 0 and supplier.id == self.pk:
            raise ValidationError('У завода не может быть поставщика.')
        if node_type == 1 and supplier is not None:
            if supplier.node_type not in [0, 2]:
                raise ValidationError(
                    'Поставщиком для розничной сети может быть только завод или индивидуальный предприниматель.')
        if node_type == 2 and supplier is not None:
            if supplier.node_type not in [0, 1]:
                raise ValidationError('Поставщиком для индивидуального предпринимателя может быть только завод.')