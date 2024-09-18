# accounts/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import InvestmentAccount, Transaction, UserInvestmentAccount
from .permissions import IsViewOnly, IsFullCRUD, IsPostOnly
from .serializers import InvestmentAccountSerializer, TransactionSerializer, UserInvestmentAccountSerializer


class InvestmentAccountViewSet(viewsets.ModelViewSet):
    queryset = InvestmentAccount.objects.all()
    serializer_class = InvestmentAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [IsViewOnly()]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsFullCRUD()]
        return super().get_permissions()


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]


# Admin endpoint
from rest_framework.decorators import action
from rest_framework.response import Response


class AdminViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='user-transactions')
    def user_transactions(self, request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)
        total_balance = transactions.aggregate(sum('amount'))

        return Response({
            'transactions': TransactionSerializer(transactions, many=True).data,
            'total_balance': total_balance['amount__sum'],
        })
