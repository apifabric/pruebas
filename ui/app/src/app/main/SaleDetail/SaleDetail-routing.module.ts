import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SaleDetailHomeComponent } from './home/SaleDetail-home.component';
import { SaleDetailNewComponent } from './new/SaleDetail-new.component';
import { SaleDetailDetailComponent } from './detail/SaleDetail-detail.component';

const routes: Routes = [
  {path: '', component: SaleDetailHomeComponent},
  { path: 'new', component: SaleDetailNewComponent },
  { path: ':id', component: SaleDetailDetailComponent,
    data: {
      oPermission: {
        permissionId: 'SaleDetail-detail-permissions'
      }
    }
  }
];

export const SALEDETAIL_MODULE_DECLARATIONS = [
    SaleDetailHomeComponent,
    SaleDetailNewComponent,
    SaleDetailDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SaleDetailRoutingModule { }